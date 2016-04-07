/* jshint node: true */

var path = require('path');
var webpack = require("webpack");

module.exports = {
    entry: './unusualbusiness/assets/scripts/main.js',
    output: {
        path: path.resolve(__dirname, './unusualbusiness/static/scripts'),
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            {
                test: /isotope\-|fizzy\-ui\-utils|imagesloaded|desandro\-|masonry|outlayer|get\-size|doc\-ready|eventie|eventemitter/,
                loader: 'imports?define=>false&this=>window'
            },
            {
                test: /\.js?$/,
                exclude: /node_modules/,
                loader: "babel",
                query: {
                    presets: ['es2015']
                }
            }
        ]
    },
    // resolve: {
    //     modulesDirectories: ["web_modules", "node_modules", "bower_components"]
    // },
    plugins: [
        // new webpack.ProvidePlugin({
        //     $: "jquery",
        //     jQuery: "jquery",
        //     "window.jQuery": "jquery"
        // })
        // new webpack.ResolverPlugin(
        //     new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin(".bower.json", ["main"])
        // )
    ],
    devtool: 'source-map',
    devtoolModuleFilenameTemplate: '[resourcePath]',
    devtoolFallbackModuleFilenameTemplate: '[resourcePath]?[hash]'
};
