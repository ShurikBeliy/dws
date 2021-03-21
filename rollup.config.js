import typescript from 'rollup-plugin-typescript'
import pkg from './package.json'

export default {
  input: 'static/typescript/main.ts',
  output: {
    sourcemap: true,
    format: 'iife',
    name: 'app',
    file: 'static/js/main.js'
  },
  external: [
    ...Object.keys(pkg.dependencies || {}),
    ...Object.keys(pkg.peerDependencies || {}),
  ],
  plugins: [
    typescript({
      typescript: require('typescript'),
    }),

  ],
};
