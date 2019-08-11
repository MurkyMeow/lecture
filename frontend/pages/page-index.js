import { State, webc, iter } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import { get } from '../api'
import css from './page-index.css'

const lecture = obj =>
  (div('.lecture')
    (div('.lecture-info').style('background', obj._`background`)
      (div('.lecture-title')(obj._`title`))
      (pre('.lecture-summary')(obj._`subtitle`))
    )
    (Progress().max(5).done([0, 2]))
  )

export const pageIndex = webc('lecture-page-index', {
  css,
  async init() {
    this.courses = new State({})
    this.courses.v = await get('/courses/')
  },
  render(h) {
    return h
    (div('.content')
      (Lesson())
      (iter(this.courses.keys, key =>
        (article()
          (h1(key))
          (section(iter(this.courses._`${key}`, lecture)))
        )
      ))
      (Button()('.link').text('Показать все'))
    )
  },
})
