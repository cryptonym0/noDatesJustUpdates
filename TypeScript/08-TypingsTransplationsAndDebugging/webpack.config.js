module.exports = {
    entry: './main-app.ts',
    output: {
        filename: './bundle.js'
    },
    devtool: 'inline-source-map',
    resolve: {
        extensions: ['.ts', '.js']
    },
    module:{
        rules: [
            {
                test: /\.ts$/,
                loader: 'ts-loader'
            },
            {
                test: /\.ts$/,
                enforce: 'pre',
                loader: 'tslint-loader'
            }
        ]
    }
}