var defaultThreads = [
    {
        id: 1,
        title: "Thread 1",
        author: "Adithya",
        date: Date.now(),
        content: "Thread content",
        comments: [
            {
                author: "Adithya",
                date: Date.now(),
                content: "Hello"
            },
            {
                author: "Abhiram",
                date: Date.now(),
                content: "Hello,how are you?"
            }
        ]
    },
    {
        id: 2,
        title: "Thread 2",
        author: "Adithya",
        date: Date.now(),
        content: "Thread content 2",
        comments: [
            {
                author: "Adithya",
                date: Date.now(),
                content: "Hello"
            },
            {
                author: "Abhiram",
                date: Date.now(),
                content: "Hello,how are you?"
            }
        ]
    }
]

var threads = defaultThreads
if (localStorage && localStorage.getItem('threads')) {
    threads = JSON.parse(localStorage.getItem('threads'));
} else {
    threads = defaultThreads;
    localStorage.setItem('threads', JSON.stringify(defaultThreads));
}