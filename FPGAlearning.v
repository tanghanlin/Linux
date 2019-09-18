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



