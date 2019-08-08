import { State, webc, iter } from 'marycat'
import { Button } from './button';
import { Progress } from './progress';
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

export const Lesson = webc({
  name: 'lecture-lesson',
  css,
  render: h => (h
    (div('.wrapper')
      (div('.content')
        (Progress().max(5))
        (div('.lesson-name')('В жизни не пригодится?'))
        (div('.course-name')('Линейная алгебра'))
        (div('.lesson-text')('Lorem ipsum, dolor sit amet consectetur adipisicing elit.'))
      )
      (div('.comment-box')
        (div('.comment-input')
          (textarea().attr('placeholder', 'Оставить комментарий'))
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
  ),
})
