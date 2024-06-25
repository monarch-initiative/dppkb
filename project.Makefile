## Add your own custom Makefile targets here


KB_NAME = dppkb
CATEGORY = Disease
COLLECTION = disease
INDEX_SLOTS = diseases

KB = kb/$(KB_NAME).yaml

test-examples: test-data validate-data

test-data: $(KB)
	yq . $<

validate-data: $(KB) $(SOURCE_SCHEMA_PATH)
	yq ea '[.]' $< | yq e '{"$(INDEX_SLOTS)": .}' - > tmp/data.yaml && \
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) tmp/data.yaml

index: kb/$(KB_NAME)-no-evidence.yaml
	curategpt index -p db -c $(COLLECTION) $< 

list:
	curategpt collections list -p db

app:
	curgptapp

%-no-evidence.yaml: %.yaml
	yq eval 'del(.. | .evidence?)' $< > $@.tmp && mv $@.tmp $@
%-clean.yaml: %.yaml
	yq . $< > $@

tmp/with-evidence.yaml:
	curategpt  citeseek --model gpt-4o $(KB) > $@.tmp && mv $@.tmp $@

normalized: kb/$(KB_NAME)-clean.yaml
	mv kb/$(KB_NAME)-clean.yaml kb/$(KB_NAME).yaml

kb-docs: derived-yaml all_html

derived-yaml:
	cd derived && yq -s '.name | sub("\\s+|[^[:alnum:]]+"; "_")' ../kb/$(KB_NAME).yaml

tmp/complete-%.yaml:
	curategpt complete  -X yaml  --model gpt-4o -p db -c $(COLLECTION) -P name "$*"   > $@

derived/%.html: derived/%.yml
	$(RUN) linkml-render -c config/render.yaml -r $(CATEGORY) -s src/$(KB_NAME)/schema/$(KB_NAME).yaml  $< -o $@

# list the yml files via shell to get the list of files
all_html: $(patsubst %.yml, %.html, $(shell find derived -name '*.yml'))
