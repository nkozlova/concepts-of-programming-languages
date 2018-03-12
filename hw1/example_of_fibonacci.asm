begin my_fibonacci
move *e **sp
pop
move *a **sp
pop
move *b **sp
pop
move *f **sp
pop
go *f 4
push *b
push *a
move *ip *e
sub *f 1
push *e
push *f
push *b
push *a
call my_fibonacci
move *a **sp
pop
move *b **sp
pop
move *c *b
add *b *a
move *a *c
move *e **sp
pop
push *b
push *a
move *ip *e
end
put_str The n-th number in fibonacci sequence (start with 0 index)
put_str Your number n:
get *a
push *a
push 1
push 0
call my_fibonacci
move *a **sp
pop
move *b **sp
pop
put_str Result:
print *b
exit
