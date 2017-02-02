// $(document).ready(() => {
//   console.log('focus', $('textarea.query')[0])
//   $('textarea.query')[0].focus()
// })

$(document).on('keypress', evt => {
  if ((evt.metaKey || evt.ctrlKey) && evt.keyCode === 13) {
    sendQuery(evt.target.value)
  }
})

let sendQuery = co.wrap(function *(query) {
  let resultTa = $('textarea.result')
  resultTa.removeClass('error').text('Executing query...')

  let response = yield fetch('http://localhost:8080/query', {
    method: 'POST',
    body: query,
  })

  if (response.status !== 200) {
    resultTa.addClass('error').text(yield response.text())
  } else {
    let text = JSON.stringify(yield response.json(), null, 2)
    resultTa.text(text)
  }
})
