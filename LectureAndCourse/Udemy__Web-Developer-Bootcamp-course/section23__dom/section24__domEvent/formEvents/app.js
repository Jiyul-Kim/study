const tweetForm = document.querySelector("#tweetForm")
const tweetContainer = document.querySelector("#tweets")
tweetForm.addEventListener('submit', function(e){
    e.preventDefault()
    // const usernameInput = document.querySelectorAll('input')[0]
    // const tweetInput = document.querySelectorAll('input')[1]
    // console.log(usernameInput.value, tweetInput.value)

    const usernamInput = tweetForm.elements.username;
    const tweetInput = tweetForm.elements.tweet;
    addTweet(usernamInput.value, tweetInput.value)
    usernamInput.value = '';
    tweetInput.value = '';


})

const addTweet = (username, tweet) => {
    const newTweet = document.createElement('li');
    const bTag = document.createElement('b')
    bTag.append(username);
    newTweet.append(bTag);
    newTweet.append(`- ${tweet}`)
    tweetContainer.append(newTweet)
}