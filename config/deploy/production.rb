set :stage, :production
set :stage_application, "p-#{fetch(:application)}"

# Simple Role Syntax
# ==================
role :app, %w{deploy@178.79.150.155}
role :web, %w{deploy@178.79.150.155}
role :db,  %w{deploy@178.79.150.155}
#role :dev,  %w{vagrant@192.168.114.143}

# Extended Server Syntax
# ======================
server '178.79.150.155', user: 'deploy', roles: %w{web app db}
#server '192.168.114.143', user: 'vagrant', password: 'vagrant', roles: %w{dev}

# you can set custom ssh options
# it's possible to pass any option but you need to keep in mind that net/ssh understand limited list of options
# you can see them in [net/ssh documentation](http://net-ssh.github.io/net-ssh/classes/Net/SSH.html#method-c-start)
# set it globally
#  set :ssh_options, {
#    keys: %w(~/.ssh/id_rsa),
#    forward_agent: false,
#    auth_methods: %w(password)
#  }

set :deploy_to, -> { "/var/www/vhosts/#{fetch(:stage_application)}" }

set :uploads_dir,  -> { "/var/www/vhosts/#{fetch(:stage_application)}/shared/web/app/uploads" }

set :dev_path, -> { "/var/www/vhosts/d-#{fetch(:application)}/current" }

set :wpcli_remote_url, -> {"http://www.#{fetch(:application)}.nl"}
#Url of the Wordpress root installation on the remote server (used by search-replace command).

set :wpcli_local_url, -> {"http://www.#{fetch(:application)}.nl.dev"}
#Url of the Wordpress root installation on the local server (used by search-replace command).

set :tmp_dir, -> { "/var/www/vhosts/#{fetch(:stage_application)}" }
#A local temp dir which is read and writeable. Defaults to /tmp.

set :local_tmp_dir, -> { "/var/www/vhosts/d-#{fetch(:application)}/current" }
#A local temp dir which is read and writeable. Defaults to /tmp.

#set :wpcli_args
#You can pass arguments directly to WPCLI using this var. By default it will try to load values from ENV['WPCLI_ARGS'].

#set :wpcli_local_uploads_dir, -> { "/Users/jeremycs/Development/dev.vm2/d-fiets-salzburg/current/web/app/uploads/" }
#Local dir where WP stores the uploads. IMPORTANT: Add trailing slash! Optional if using Bedrock Wordpress Stack

#set :wpcli_remote_uploads_dir, -> { "/var/www/vhosts/s-#{fetch(:application)}/shared/web/app/uploads/" }
#Remote dir where WP stores the uploads. IMPORTANT: Add trailing slash! Optional if using Bedrock Wordpress Stack

fetch(:default_env).merge!(wp_env: :production)

