import { webc } from 'marycat'
import css from './button.css'

export const Button = webc('lecture-button', {
  css,
  props: {
    text: '',
  },
  render: (h, { text }) => (h
    (span(text).tabindex(0))
  ),
})
