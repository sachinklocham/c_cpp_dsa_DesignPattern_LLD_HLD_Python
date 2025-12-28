A function can return one of several possible types, as long as they are all wrapped inside a single return type such as:

std::variant<>

std::any

std::optional<>

a polymorphic base pointer / reference

So it’s not “return any type freely” — it’s:

return one well-defined type that can hold multiple alternatives

std::variant makes that explicit and type-safe.

What your example means
auto make(bool flag) -> std::variant<int, std::string> {
    if (flag) return 10;
    return "ten";
}
return 10;      // becomes variant{ int{10} }
return "ten";   // becomes variant{ std::string{"ten"} }