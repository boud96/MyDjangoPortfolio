import { run } from '../js/play-core/run.js'
import * as backgroundProgram from './ascii-background-program.js'

const reducedMotion = window.matchMedia &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches
const canvas = document.getElementById('ascii-background')

if (canvas && !reducedMotion) {
  run(backgroundProgram, {
    element: canvas,
    renderer: 'canvas',
    fps: 24,
    allowSelect: false
  }, {
    name: canvas.dataset.name || ''
  }).catch(function(error) {
    console.error('ASCII background failed to initialize:', error)
  })
}
