import { State, webc, iter, textarea } from 'marycat'
import { Button } from './button'
import { Progress } from './progress'
import css from './lesson.css'

const comments = new State([
  {
    user: { name: 'rulon oboev', photo: '' },
    text: 'cool',
  },
  {
    user: { name: 'fabric zavodov', photo: '' },
    text: 'fancy',
  },
])

export const Lesson = webc('lecture-lesson', {
  css,
  props: {
    slide: 0,
    data: {},
  },
  render: (h, { slide, data }) => (h
    (div('.wrapper').tabindex(0)
      .keydown(e => {
        switch (e.code) {
          case 'ArrowLeft': return slide.v > 0 && slide.v--
          case 'ArrowRight': return slide.v < 5 - 1 && slide.v++
        }
      })
      (div('.content')
        (Progress().max(5).active(slide))
        (iframe().attr('src', slide.after(v =>
          `/course/${data.v.name}/${data.v.index + 1}/#${v}`)
        ))
      )
      (div('.comment-box')
        (div('.comment-input')
          (textarea().placeholder('Оставить комментарий'))
          (Button().text('📡'))
        )
        (iter(comments, x =>
          (div('.comment')
            (img().attr('src', x._`user`._`photo`))
            (div()
              (div('.comment-author')(x._`user`._`name`))
              (div('.comment-text')(x._`text`))
            )
          )
        ))
      )
    )
    ($el => {
      const f = $el.querySelector('iframe')
      f.onload = () => f.style.height = `${f.contentWindow.innerHeight + 50}px`
    })
  ),
})
