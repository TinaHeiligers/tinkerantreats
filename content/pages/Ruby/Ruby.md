Title: Ruby projects
Date: 2016-07-31
Category: Ruby

This folder is for Ruby-only work. Ruby on Rails is in the {Rails folder}content/Rails

# Tutorials with Code
6 Ruby Best Practices Beginners Should Know](https://www.codementor.io/ruby-on-rails/tutorial/6-ruby-best-practices-beginners-should-know) is a fantastic read, concise and gives code to demonstrate the ideas.
A definate afternooner or eveninger to work through.
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
