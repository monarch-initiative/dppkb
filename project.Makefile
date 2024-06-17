## Add your own custom Makefile targets here

KB = kb/dppkb.yaml

test-data: $(KB)
	yq . $<

validate-data: $(KB) $(SOURCE_SCHEMA_PATH)
	yq ea '[.]' $< | yq e '{"diseases": .}' - > tmp/data.yaml && \
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) tmp/data.yaml

index: kb/dppkb-no-evidence.yaml
	curategpt index -p db -c disease $< 

list:
	curategpt collections list -p db

app:
	curgptapp

%-no-evidence.yaml: %.yaml
	yq eval 'del(.. | .evidence?)' $< > $@.tmp && mv $@.tmp $@
%-clean.yaml: %.yaml
	yq . $< > $@

tmp/with-evidence.yaml:
	curategpt  citeseek --model gpt-4o $(KB) > $@

normalized: kb/dppkb-clean.yaml
	mv kb/dppkb-clean.yaml kb/dppkb.yaml

kb-docs: derived-yaml all_html

derived-yaml:
	cd derived && yq -s '.name | sub("\\s+|[^[:alnum:]]+"; "_")' ../kb/dppkb.yaml

tmp/complete-%.yaml:
	curategpt complete  -X yaml  --model gpt-4o -p db -c disease -P name "$*"   > $@

derived/%.html: derived/%.yml
	$(RUN) linkml-render -c config/render.yaml -r Disease -s src/dppkb/schema/dppkb.yaml  $< -o $@

# list the yml files via shell to get the list of files
all_html: $(patsubst %.yml, %.html, $(shell find derived -name '*.yml'))
