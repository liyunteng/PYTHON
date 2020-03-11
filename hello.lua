#!/usr/bin/lua
--[[
print("Hello, world!")
print("aabbcc")
--]]
print("Hello")

function factorial(n)
   if n == 0 then
      return 1
   else
      return n * factorial(n-1)
   end
end

print(factorial(10))

function testFun(tab, fun)
   for k,v in pairs(tab) do
      print(fun(k, v))
   end
end

tab1 = {key1="val1", key2="val2"}
testFun(tab1,
        function(k, v)
           return k.." = "..v
        end
)

for i = 10, 1, -1 do
   repeat
      if i == 5 then
         print("continue code here")
         break
      end
      print(i, "loop code here")
   until true
end

if (0) then
   print("0 is true")
end


function max(num1, num2)
   if (num1 > num2) then
      result = num1
   else
      result = num2
   end
   return result
end

print(max(10, 4))
print(max(4, 10))

myprint =
   function(param)
      print("This is function - ##", param, "##")
   end

function add(num1, num2, fp)
   result = num1 + num2
   fp(result)
end
add(1, 2, myprint)


s, e = string.find("www.runoob.com", "runoob")
print(s, e)

function maximum(a)
   local mi = 1
   local m = a[mi]
   for i,val in ipairs(a) do
      if val>m then
         mi = i
         m = val
      end
   end
   return m, mi
end

print(maximum({8, 10, 23, 12, 5}))


function average(...)
   result = 0
   local arg={...}
   for i, v in ipairs(arg) do
      result = result + v
   end
   print("total " .. #arg .." arg")
   return result/#arg
end

print(average(10, 5, 3, 4, 5, 6))


-- function fwrite(fmt, ...)
--    return io.write(string.format(fmt, ...))
-- end

-- fwrite("runoob\n")
-- fwrite("%d%d\n", 1, 2)

do
   function foo(...)
      for i = 1, select("#", ...) do
         local arg = select(i, ...)
         print("arg", arg)
      end
   end
   foo(1, 2, 3, 4)
end


s = "This is a string"
print(string.upper(s))
print(string.lower(s))
print(string.gsub(s, "string", "test"))
print(string.find(s, "string"))
print(string.reverse(s))
print(string.format("%s", s))
print(string.char(97, 98, 99, 100))
print(string.byte("abcd"))
print(string.len(s))
print(string.rep(s, 3))
print(string.match(s, "%a+ %a+ %a+ %a+"))
for word in string.gmatch(s, "%a+") do
   print(word)
end



co = coroutine.create(
   function(i)
      print(i)
   end
)

coroutine.resume(co, 1)
print(coroutine.status(co))

print('----------')

co = coroutine.wrap(
   function(i)
      print(i)
   end
)
co(1)

print('----------')

co2 = coroutine.create(
   function()
      for i = 1, 10 do
         print(i)
         if i == 3 then
            print(coroutine.status(co2))
            print(coroutine.running())
         end
         coroutine.yield()
      end
   end
)
coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)

print(coroutine.status(co2))
print(coroutine.running())

coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)


f = io.open('hello.lua', 'r')
io.input(f)
-- print(io.read("*n"))
-- print(io.read("*a"))
print(io.read("*l"))
io.close(f)

-- f = io.open('hello.lua', 'a')
-- io.output(f)
-- io.write('-- hello.lua')
-- io.close(f)
