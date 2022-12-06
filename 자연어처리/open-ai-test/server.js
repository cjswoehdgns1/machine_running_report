var express = require('express');
var app = express();
var request = require('request');
var { OpenAIApi, Configuration } = require('openai');

/**
 * 입력 후 대기시간동안 기다리는 채팅 표시 추가해야 함
 * ...같은 것을 response랑 치환하면 될듯
 */

const configuration = new Configuration({
    apiKey: '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',
});
const openai = new OpenAIApi(configuration);

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html')
})

var client_id = '4rLzyu8vanCZVfb8AiJS';
var client_secret = 'dTcX7ZnAYr';

app.get('/translate', function(req, res) {
    var api_url = 'https://openapi.naver.com/v1/papago/n2mt';
    var query = req.query.q;

    var options = {
        url: api_url,
        form: {'source': 'ko', 'target':'en', 'text':query},
        headers: {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    }
    request.post(options, function(error, response, body) {
        var eng = JSON.parse(body).message?.result.translatedText;
    
        openai.createCompletion({
            model: "text-davinci-003",
            prompt: document.querySelector('#input').value,
            temperature: 0.7,
            max_tokens: 256,
            top_p: 1,
            frequency_penalty: 0,
            presence_penalty: 0,
            }).then((result) => {
                
                var template = `<div class="line">
                    <span class="chat-box">${ result.data.choices[0].text }</span>
                </div>`;
                document.querySelector('.chat-content').insertAdjacentHTML('beforeend',
                template)
            });
    })
})

app.listen(3000, function() {
    console.log('http://localhost:3000/translate app listening on port 3000!')
})

