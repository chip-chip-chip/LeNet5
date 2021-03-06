-- Generic Counter --

-- high-speed/low-power group
-- Fiore, Neri, Zheng
-- 
-- keyword in MAIUSCOLO (es: STD_LOGIC)
-- dati in minuscolo (es: data_in)
-- segnali di controllo in MAIUSCOLO (es: EN)
-- componenti instanziati con l'iniziale maiuscola (es: Shift_register_1)
-- i segnali attivi bassi con _n finale (es: RST_n)


----------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.math_real.all;

entity counter_N is

generic (n : integer:=10);
port (enable, clk, rst : in std_logic;
		count : out std_logic_vector(natural(ceil(log2(real(n))))-1 downto 0);
		tc : out std_logic);
end counter_N;

architecture behavior of counter_N is
signal contatore : unsigned(natural(ceil(log2(real(n))))-1 downto 0);

begin

process (clk,rst)
begin

	if (clk'event and clk='1') then

if rst='1' then
		contatore<= (others => '0');
		tc <= '0';
elsif (rst='0') then

	
		if enable='1' then
			if (contatore = n-1) then
				contatore<=(others => '0');
				tc <= '1';
			else
				contatore <= contatore+1;
				tc <= '0';
			end if;
		end if;
	end if;
end if;
if (contatore = n-1) then
		tc <= '1';
else
		tc <= '0';
end if;
end process;

count <= std_logic_vector(contatore);

end behavior;