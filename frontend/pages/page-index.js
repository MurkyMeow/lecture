import { State, webc, iter, _if } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import { get } from '../api'
import css from './page-index.css'

const lecture = (obj, onclick) =>
  (div('.lecture').click(onclick)
    (div('.lecture-info').style('background', obj._`background`)
      (div('.lecture-title')(obj._`title`.or('')))
      (pre('.lecture-summary')(obj._`subtitle`.or('')))
    )
    (Progress().max(5).done([0, 2]))
  )

export const pageIndex = webc('lecture-page-index', {
  css,
  async init() {
    this.lecture = new State(null)
    this.courses = new State({})
    this.courses.v = await get('/static/preview.json')
  },
  render(h) {
    return h
    (div('.content')
      (_if(this.lecture)
        (Lesson().data(this.lecture).stop().click(_=>_))
      )
      (iter(this.courses.keys, key =>
        (article()
          (h1(key))
          (section(iter(this.courses._`${key}`, (lec, i) =>
            lecture(lec, () => this.lecture.v = { ...lec.v, name: key.v, index: i.v })
          )))
        )
      ))
      (Button('.link').text('Показать все'))
    )
  },
})
