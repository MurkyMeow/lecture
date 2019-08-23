import { State, webc, iter, _if } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import { get } from '../api'
import css from './page-index.css'

export const pageIndex = webc('lecture-page-index', {
  css,
  render(h) {
    const lecture = new State(null)
    const courses = new State({})
    get('/static/preview.json').then(data => courses.v = data)
    return h
    (div('.content')
      (_if(lecture)
        (Lesson().data(lecture).on('hide', () => lecture.v = null))
      )
      (iter(courses.keys, key =>
        (article()
          (h1(key))
          (section(iter(courses._`${key}`, (lec, i) =>
            (div('.lecture')
              .click(() => lecture.v = { ...lec.v, name: key.v, index: i.v })
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
