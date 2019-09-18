always@(posedge clk, negedge rst_n)
    if(!rst_n) d <= 1'b0

posedge //上升沿触发(高电平复位)
negedge //下降沿触发(低电平复位)
always@() //拥有两个参数变量，第一个代表触发，第二个代表电平复位

/*两种数据类型wire和reg的使用方法
1.输入信号无需定义数据类型
2.输入输出信号缺省类型为wire
3.inout双向端口类型只能是wire
4.always过程块中赋值的变量必须是reg
*/




module block(a, b, c, d, clk);
    input a, b, clk;
    output c;
    reg d;
        assign c = a & ~b;
    always@(posedge clk);
        d <= c;
endmodule;
//  <<为左移符号， >>为右移符号， 与C语言一致
    
//同一个module中语句为并行执行，但always中，begin与end之间是顺序执行的


wait//语句会一直在代码程序中等待，直到满足括号中的条件后，执行其中的语句

assign//只能对wire变量赋值，不可以对reg变量赋值

//在initial语句中，若使用了assign语句后，变量无法普通的进行赋值，只能使用assign语句，或者用deassign语句解除连续赋值状态

assign,force//语句中，可使用force强制连续赋值，当release后，若变量之前被assign连续赋值，则该变量恢复为assign驱动
