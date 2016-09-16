Title: Ruby projects
Date: 2016-09-16
Category: Ruby

This folder is for Ruby-only work. Ruby on Rails is in the Ruby on Rails tab.

# Tutorials with Code
[6 Ruby Best Practices Beginners Should Know](https://www.codementor.io/ruby-on-rails/tutorial/6-ruby-best-practices-beginners-should-know) is a fantastic read, concise and gives code to demonstrate the ideas.

For example, avoiding loops in Ruby:
Don't do
 ```
for elem in [1, 2, 3, 4, 5]
puts elem
end
```
Do do:
```
[1, 2, 3, 4, 5].each do |elem|
    puts elem
end
```
Or even better:
```
[1, 2, 3, 4, 5].each do { |elem| puts elem }
```
