fn main() {
    // entry point of rust program

    println!("Hello, world!"); // ! at the end of macro indicates that it is a macro call
    let apples_in_garden = 50; // variable binding , assignment,  snakeCase, i32 deduced 
    // {} is a placeholder for value to be printed
    println!("Apples in garden: {}", apples_in_garden);
    let oranges = 30+10; // variable binding, assignment, snakeCase, i32 deduced
    println!("Oranges in garden: {}", oranges);
    println!("Total fruits in garden: {}", apples_in_garden + oranges);
    
}
