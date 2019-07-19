// $("#Title").css("color","green");
//
//

// var obj = JSON.parse(post_j)

var a = ['1','2','3']


a.forEach(function(entry){
  console.log(entry)
});

var obj = JSON.parse(post_j)

var count = 0

for(var key in obj){
  if(obj.hasOwnProperty(key)){
    count = count + 1
    var val = obj[key]
    console.log(key)
    console.log(val)
  }
}

console.log(obj)
console.log(count)
