# �����C���X�g�{���A�v��

## ���[�J�����ł̎��s
0. �� : Windows 10 Pro

1. ���|�W�g�����_�E�����[�h����B
```
git clone https://github.com/wakadorimk2/VueApplication
```

2. Twitter�A�J�E���g�̃g�[�N�����擾����B
   1. Twitter�A�J�E���g��p�ӂ���B(API����s���Ɛ�����H�炤�̂ŁA�ʃA�J���������߁B)
   2. [Twitter Developer](https://developer.twitter.com/en/apps)�ɃA�N�Z�X����B
   3. ```Create an app```�ŃA�v�����쐬���A```Details```�ŃA�v���ڍׂ�\������B
      | <img src="img/twitter_developer.png" width=500> |
      | :-: |
      | �g�[�N���̏��� |
   4. �쐬�����A�v���̃g�[�N��4���擾����B
      - API key
      - API secret key
      - Access token
      - Access token secret

      | <img src="img/tokens.png" width=500> |
      | :-: |
      | Twitter�A�J�E���g�̃g�[�N�� |

3. ```server/conf_secret.py```���쐬���A�g�[�N������͂���B
```
keys_and_tokens = {
    'consumer_key' : '[API key]',
    'consumer_secret' : '[API secret key]',
    'access_token_key' : '[Access token]',
    'access_token_secret' : '[Access token secret]',
}
```

4. ���C�u�����̃C���X�g�[��
   1. npm��Vue CLI���C���X�g�[������B
   2. Vue.js���C�u�������C���X�g�[������B
      ```
      cd vue
      npm install
      ```
   3. Python���C�u�������C���X�g�[������B
      ```
      cd server
      pip install -r requirements.txt
      ```

5. ���s
   1. Python�T�[�o���N������B
      ```
      cd server
      python server.py
      ```
   2. Vue.js�N���C�A���g���N������B
      ```
      cd vue
      npm run serve
      ```


# �Q�l
- Developing a Single Page App with Flask and Vue.js | TestDriven.io https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

- [Vue.js �� vue-cli ���g���ăV���v���ɂ͂��߂Ă݂� - Qiita](https://qiita.com/567000/items/dde495d6a8ad1c25fa43)

- [imlinus/vue-magic-grid: ??��?? Responsive Magic Grid for Vue](https://github.com/imlinus/vue-magic-grid)

- [HTML/CSS�̊o�����@WEB����ɖ𗧂֗��ȃ`�[�g�V�[�g�܂Ƃ� - Minimal Green](https://www.atmarkit.co.jp/fdotnet/chushin/cheatsheet_02/cheatsheet_02_01.html)  

- [Twitter��API���� [2019/11/17����] - Qiita](https://qiita.com/mpyw/items/32d44a063389236c0a65)  
```/favorites/list```��15��������75���N�G�X�g(=5[���N�G�X�g/��])�̐���������̂ŉ\�Ȍ���L���b�V���O����B�܂�1���N�G�X�g��1�`200�c�C�[�g���擾�ł���̂ŁA��ɍő��200�c�C�[�g���擾���邱�Ƃ�Rate Limit�������B

- [�yTwitter�z�A�N�Z�X�g�[�N���擾�܂ł̗��� - Qiita](https://qiita.com/kiyocy24/items/833280f2536b1d3ea41e)