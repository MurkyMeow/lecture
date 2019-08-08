import { webc, iter } from 'marycat'
import css from './progress.css'

export const Progress = webc({
  name: 'lecture-progress',
  css,
  props: {
    max: 4,
    done: [],
  },
  render(h, { max, done }) {
    const items = max.after(v => [...Array(v).keys()])
    return h
    (iter(items, (_, i) => {
      const active = done.after(v => v.includes(i.v))
      return (span().class(active.tern('active', '')))
    }))
  },
})
