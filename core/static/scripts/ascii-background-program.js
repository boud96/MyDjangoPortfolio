/**
@author ertdfgcvb-inspired
@title  Name Swirl
@desc   Canvas-rendered swirl field using the portfolio owner's name.
*/

export const settings = {
  fps: 18,
  renderer: 'canvas',
  backgroundColor: 'rgba(30, 31, 34, 0)',
  color: 'rgba(255, 255, 255, 0.12)',
  fontFamily: 'Consolas, "Lucida Console", "Courier New", monospace',
  fontSize: '14px',
  lineHeight: '18px'
}

const { atan2, cos, floor, max, min, sin, sqrt } = Math
const fallbackSequence = ' ~ ./\\|_-=+*#@<>[]{}() '

export function main(coord, context, cursor, buffer, userData) {
  const text = getTextSource(userData.name)
  const t = context.time * 0.00011
  const centerX = context.cols * 0.5
  const centerY = context.rows * 0.5
  const x = (coord.x - centerX) * context.metrics.aspect
  const y = coord.y - centerY
  const radius = sqrt(x * x + y * y)
  const angle = atan2(y, x)

  const spiral =
    sin(radius * 0.18 - angle * 4.6 + t * 5.2) +
    sin(radius * 0.08 + angle * 7.4 - t * 3.1) * 0.72 +
    sin((x * 0.09 + y * 0.05) + t * 2.0) * 0.34
  const field = spiral
  const band = smoothstep(-1.35, 1.5, field)
  const edgeFade = 1 - smoothstep(min(context.cols, context.rows) * 0.46, min(context.cols, context.rows) * 0.72, radius)
  const blankMask = sin(coord.x * 0.72 + coord.y * 1.17 + field * 2.8)
  const textIndex = floor(coord.x * 0.62 + coord.y * 1.08 + field * 9 + context.frame * 0.045)
  const char = text[positiveModulo(textIndex, text.length)]

  if (char === ' ' || blankMask < -0.22 || band < 0.38) {
    return ' '
  }

  const opacity = min(0.42, max(0.04, band * edgeFade * 0.28))
  const warmth = floor(176 + band * 58)

  return {
    char,
    color: `rgba(255, ${warmth}, 138, ${opacity})`
  }
}

function getTextSource(name) {
  const source = String(name || '')
    .trim()
    .replace(/\s+/g, ' ')

  return source ? `${source}   ` : fallbackSequence
}

function positiveModulo(value, length) {
  return ((value % length) + length) % length
}

function smoothstep(edge0, edge1, value) {
  const x = min(1, max(0, (value - edge0) / (edge1 - edge0)))

  return x * x * (3 - 2 * x)
}
