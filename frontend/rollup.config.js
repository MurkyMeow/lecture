import resolve from 'rollup-plugin-node-resolve'
import postcss from 'rollup-plugin-postcss'
import serve from 'rollup-plugin-serve'
import { terser } from 'rollup-plugin-terser'
import Precss from 'precss';

const dev = process.env.ROLLUP_WATCH;

const precss = Precss({
  features: {
    'focus-within-pseudo-class': false,
  },
})

export default {
  input: 'index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    sourcemap: true,
  },
  plugins: [
    resolve({ browser: true }),
    postcss({
      plugins: [precss],
    }),
    !dev && terser(),
    dev && serve(),
  ],
}
