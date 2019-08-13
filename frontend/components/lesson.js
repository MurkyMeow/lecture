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
  render(h, { slide, data }) {
    const { name, index } =  data.v
    const slides = new State(0)
    const onload = async ({ target }) => {
      await target.contentWindow.load
      slides.v = target.contentWindow.slides.length
    }
    h($el => { // marycat, please fix
      $el.host.addEventListener('click', () => this.emit('hide'))
    })
    return h
    (div('.wrapper').prevent().stop().click(_=>_)
      .tabindex(0)
      .keydown(e => {
        switch (e.code) {
          case 'ArrowLeft': return slide.v > 0 && slide.v--
          case 'ArrowRight': return slide.v < slides.v - 1 && slide.v++
        }
      })
      (div('.content')
        (Progress().max(slides).active(slide)
          .on('change', e => slide.v = e.detail)
        )
        (iframe().on('load', onload)
          .attr('height', '300px')
          .attr('src', slide.after(v => `/course/${name}/${index + 1}/#${v}`))
        )
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
  },
})
