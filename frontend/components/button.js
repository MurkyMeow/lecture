import { webc } from 'marycat'
import css from './button.css'

export const Button = webc({
  name: 'lecture-button',
  css,
  props: {
    text: '',
  },
  fun: (h, { text }) => (h
    (span(text).attr('tabindex', 0))
  ),
})
