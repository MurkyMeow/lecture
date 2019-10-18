import resolve from 'rollup-plugin-node-resolve'
import postcss from 'rollup-plugin-postcss'
import typescript from 'rollup-plugin-typescript2'
import { terser } from 'rollup-plugin-terser'
import postcssEnv from 'postcss-preset-env'

const dev = process.env.ROLLUP_WATCH

export default {
  input: 'index.ts',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    sourcemap: true,
  },
  plugins: [
    resolve({ browser: true }),
    postcss({
      inject: false,
      minimize: !dev,
      plugins: [
        postcssEnv({
          stage: 3,
          features: {
            'nesting-rules': true,
          }
        })
      ],
    }),
    typescript(),
    !dev && terser(),
  ],
}
