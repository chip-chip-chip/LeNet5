library verilog;
use verilog.vl_types.all;
entity SNPS_CLOCK_GATE_HIGH_LeNet5_top_145 is
    port(
        CLK             : in     vl_logic;
        EN              : in     vl_logic;
        ENCLK           : out    vl_logic;
        TE              : in     vl_logic
    );
end SNPS_CLOCK_GATE_HIGH_LeNet5_top_145;
