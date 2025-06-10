const greet=(name,callback) => {
    console.log(name)
    callback()
}
greet("ram",()=> console.log("bye"))