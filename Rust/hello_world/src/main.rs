fn main() {
    // entry point of rust program

    println!("Hello, world!"); // ! at the end of macro indicates that it is a macro call
    let apples_in_garden = 50; // variable binding , assignment,  snakeCase, i32 deduced 
    // {} is a placeholder for value to be printed
    println!("Apples in garden: {}", apples_in_garden);
    let oranges = 30+10; // variable binding, assignment, snakeCase, i32 deduced
    println!("Oranges in garden: {}", oranges);
    println!("Oranges in garden: {} apples in garden {}", oranges, apples_in_garden); // multiple placeholders oranges at 0 position , apples_in_garden at 1 position
    println!("Total fruits in garden: {}", apples_in_garden + oranges);
    println!("Apples in garden: {}",apples_in_garden); // positional arguments in format string  
    println!("Apples in garden: {apples_in_garden}"); // named arguments in format string   
    
    //{} is a placeholder for value to be printed indexed from 0 left to right 
    println!("Fruits in garden: {0} apples and {1} oranges where to get {0} more apples, and {1} more oranges", apples_in_garden, oranges);//apples_in_garden is at 0 index and oranges ar 1 index we can refer them multiple times in string with indexes

   // let fruits = apples_in_garden + oranges; // variable binding, assignment, snakeCase, i32 deduced. if we do not use fruits variable then compiler will give warning warning: unused variable: `fruits` so mark as _ in begginning of variable
    //println!("Total fruits in garden: {fruits}"); // named argument in format string

    let _fruits = apples_in_garden + oranges; // _ in begginning of variable to supress compiler warning
    
}
