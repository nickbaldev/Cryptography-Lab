# tools
CC := gcc
RM := rm -f

# flags
CFLAGS := -m32 -ggdb -Wall

EXECUTABLES = random_keygen random_time random_time_attack

# these are the compilation rules
all: $(EXECUTABLES)

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	$(RM) $(EXECUTABLES)
