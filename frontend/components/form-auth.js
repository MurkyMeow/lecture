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
      (input().type('email').placeholder('Email'))
      (input().type('password').placeholder('Пароль'))
      (_if(signup)
        (input().type('password').placeholder('Повторите пароль'))
      )
      (Button().text('Продолжить'))
    )
  ),
})
