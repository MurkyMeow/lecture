import { webc, _if } from 'marycat'
import { Button } from './button'
import css from './form-auth.css'

export const FormAuth = webc({
  name: 'lecture-form-auth',
  css,
  props: {
    signup: true,
  },
  fun: (h, { signup }) => (h
    (form()
      (input('@email').type('email')
        .placeholder('Email')
        .required()
      )
      (input('@password').type('password')
        .placeholder('Пароль')
        .required()
      )
      (_if(signup)
        (input('@password_again').type('password')
          .placeholder('Повторите пароль')
          .required()
        )
      )
      (Button().text('Продолжить'))
    )
  ),
})
