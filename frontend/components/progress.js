import { webc, iter } from 'marycat'
import css from './progress.css'

export const Progress = webc({
  name: 'lecture-progress',
  css,
  props: {
    max: 4,
    done: [],
    active: -1,
  },
  render(h, { max, done, active }) {
    const items = max.after(v => [...Array(v).keys()])
    return h
    (iter(items, (_, i) => {
      const isdone = done.after(v => v.includes(i.v))
      const isactive = active.eq(i)
      return (span()
        .click(() => active.v = i.v)
        .attr('data-done', isdone)
        .attr('data-active', isactive)
      )
    }))
  },
})
