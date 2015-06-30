set :application, 'unusualbusiness'
set :repo_url, 'git@github.com:jeremy-c/unusualbusiness.git'
set :theme_name, 'unusualbusiness'

# Branch options
# Prompts for the branch name (defaults to current branch)
#ask :branch, -> { `git rev-parse --abbrev-ref HEAD`.chomp }

# Hardcodes branch to always be master
# This could be overridden in a stage config file
set :branch, :master

# Use :debug for more verbose output when troubleshooting
set :log_level, :info

# Apache users with .htaccess files:
# it needs to be added to linked_files so it persists across deploys:
set :linked_files, fetch(:linked_files, []).push('.env', 'web/.htaccess')
#set :linked_files, fetch(:linked_files, []).push('.env')
set :linked_dirs, fetch(:linked_dirs, []).push('web/app/uploads')


namespace :deploy do
  desc 'Restart application'
  task :restart do
    on roles(:app), in: :sequence, wait: 5 do
      # Your restart mechanism here, for example:
      # execute :service, :nginx, :reload
    end
  end
end

# The above restart task is not run by default
# Uncomment the following line to run it on deploys if needed
# after 'deploy:publishing', 'deploy:restart'

namespace :deploy do
  desc 'Update WordPress template root paths to point to the new release'
  task :update_option_paths do
    on roles(:app) do
      within fetch(:release_path) do
        if test :wp, :core, 'is-installed'
          [:stylesheet_root, :template_root].each do |option|
            # Only change the value if it's an absolute path
            # i.e. The relative path "/themes" must remain unchanged
            # Also, the option might not be set, in which case we leave it like that
            value = capture :wp, :option, :get, option, raise_on_non_zero_exit: false
            if value != '' && value != '/themes'
              execute :wp, :option, :set, option, fetch(:release_path).join('web/wp/wp-content/themes')
            end
          end
        end
      end
    end
  end
end

# The above update_option_paths task is not run by default
# Note that you need to have WP-CLI installed on your server
# Uncomment the following line to run it on deploys if needed
# after 'deploy:publishing', 'deploy:update_option_paths'


######################################
###########  Linksmith  ##############
######################################

namespace :linksmith do
  desc 'Update deploy directory user and group ownership'
  task :setup_deploy_dir_ownership do
    on roles(:app) do
      info " Running chown on #{fetch(:deploy_to)}"
      execute "chown -R deploy:deploy #{fetch(:deploy_to)}"

      info " Running chmod on #{fetch(:deploy_to)}"
      execute "chmod -R g+s #{fetch(:deploy_to)}"
    end
  end
end
before 'deploy:starting', 'linksmith:setup_deploy_dir_ownership'

namespace :linksmith do
  desc 'Update upload directory user and group ownership'
  task :setup_upload_group_ownership do
    on roles(:app) do
      info " Running chown on /uploads"
      execute "chown -R deploy:www-data #{fetch(:uploads_dir)}"

      info " Running chmod on /uploads"
      execute "chmod -R g+s #{fetch(:uploads_dir)}"
    end
  end
end
after 'deploy:starting', 'linksmith:setup_upload_group_ownership'

# The above update_option_paths task is not run by default
# Note that you need to have WP-CLI installed on your server
# Uncomment the following line to run it on deploys if needed
# after 'deploy:publishing', 'deploy:update_option_paths'



namespace :linksmith do

  # Theme path
  set :theme_path, Pathname.new('web/app/themes').join(fetch(:theme_name))

  # Local Paths
  set :local_theme_path, Pathname.new(File.dirname(__FILE__)).join('../').join(fetch(:theme_path))
  set :local_dist_path, fetch(:local_theme_path).join('dist')

  task :compile do
    run_locally do
      within fetch(:local_theme_path) do
        execute :gulp, '--production'
      end
    end
  end

  task :copy do
    on roles(:web) do

      # Remote Paths (Lazy-load until actual deploy)
      set :remote_dist_path, -> { release_path.join(fetch(:theme_path)).join('dist') }

      info " Your local distribution path: #{fetch(:local_dist_path)} "
      info " Boom!!! Your remote distribution path: #{fetch(:remote_dist_path)} "
      info " Uploading files to remote "
      upload! fetch(:local_dist_path).to_s, fetch(:remote_dist_path), recursive: true
    end
  end

  task assets: %w(compile copy)
end

after 'deploy:updated', 'linksmith:assets'