import resolve from 'rollup-plugin-node-resolve'
import { terser } from 'rollup-plugin-terser'

const dev = process.env.ROLLUP_WATCH;

export default {
  input: 'index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    sourcemap: true,
  },
  plugins: [
    resolve({ browser: true }),
    !dev && terser(),
  ],
}
