import { State, webc, iter, _if } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import { get } from '../api'
import css from './page-index.css'

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
        (Lesson().data(this.lecture)
          .on('hide', () => this.lecture.v = null)
        )
      )
      (iter(this.courses.keys, key =>
        (article()
          (h1(key))
          (section(iter(this.courses._`${key}`, (lec, i) =>
            (div('.lecture')
              .click(() => this.lecture.v = { ...lec.v, name: key.v, index: i.v })
              (div('.lecture-info').style('background', lec._`background`)
                (div('.lecture-title')(lec._`title`.or('')))
                (pre('.lecture-summary')(lec._`subtitle`.or('')))
              )
              (Progress().max(5).done([0, 2]))
            )
          )))
        )
      ))
      (Button('.link').text('Показать все'))
    )
  },
})
