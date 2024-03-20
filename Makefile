# Shell wildcard to list all circom files
CIRCOM_FILES := $(wildcard */*.circom)

r1cs: $(CIRCOM_FILES:.circom=.r1cs)
sym: $(CIRCOM_FILES:.circom=.sym)

# Wildcard rule to compile circom into r1cs
%.r1cs: %.circom
	circom $< --r1cs --sym -o $(dir $@)

%.sym: %.circom
	circom $< --r1cs --sym -o $(dir $@)

clean:
	rm -f $(CIRCOM_FILES:.circom=.r1cs) $(CIRCOM_FILES:.circom=.sym)