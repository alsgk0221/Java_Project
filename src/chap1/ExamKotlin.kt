fun main() {
    val res = sumfunc()
    println(res)
}

fun sumfunc() : Int{
    var sum = 0
    for(i in 1..100) {
        sum += i
    }
    return sum

}