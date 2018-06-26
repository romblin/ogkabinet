require('babel-polyfill');
// Webpack config for development
const path = require('path');
const postcssPresetEnv = require('postcss-preset-env');
const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  context: __dirname,
  entry: {
    metrika: './metrika/index.js',
    direct: './direct/index.js',
  },
  devServer: {
    contentBase: './static'
  },
  output: {
    path: path.resolve(__dirname, '../dist'),
    filename: '[name].js',
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      },
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      // {
      //   test: /\.(scss|css)$/,
      //   loader: ExtractTextPlugin.extract({
      //     fallback: 'style-loader',
      //     // use: 'css-loader?minimize&modules&importLoaders=2&sourceMap&localIdentName=[local]!sass-loader?outputStyle=expanded&sourceMap!postcss-loader'
      //     use: [
      //       {
      //         loader: 'css-loader',
      //         options: {
      //           modules: true,
      //           importLoaders: 2,
      //           minimize: true,
      //           localIdentName: '[local]'
      //         }
      //       },
      //       {
      //         loader: 'sass-loader'
      //       },
      //       {
      //         loader: 'postcss-loader',
      //         options: {
      //           ident: 'postcss',
      //           plugins: () => [
      //             postcssPresetEnv(),
      //             autoprefixer()
      //           ]
      //         }
      //       }
      //     ]
      //   })
      // },
    ]
  },
  plugins: [
    new ExtractTextPlugin("styles.css"),
  ]
};
