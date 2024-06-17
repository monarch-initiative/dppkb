# dppkb

Disease Pathophysiology Knowledge Base FOR DEMO PURPOSES

## Website

[https://monarch-initiative.github.io/dppkb](https://monarch-initiative.github.io/dppkb)

## What is this?

This is an experiment in using CurateGPT for de-novo human-driven Knowledge Base cuation.

The general workflow is:

1. A human writes some sample YAML files for a few entries
   - the schema can be invented "on the fly"
2. Iterate using claude.ai
   - ask it to suggest other fields
   - use as a template to create more
3. Save as a .yaml file
4. Iterate with curate-gpt
   - `complete` command will generate a new entry
   - `citeseek` command will add support/refute evidence from pubmed
   - `update` command will enrich specific fields
   - `review` command will use LLM as a critic and suggest changes


## Files

- [kb/dppkb.yaml](kb/dppkb.yaml) - main KB


## Details

### Create an CurateGPT index

Run

`make index`

This should be run periodically - it makes a local ChromaDB that will be used for RAG

### Generate a new entity

Run this:

`make tmp/complete-Tuberculosis.yaml`

This uses RAG/DRAGON-AI to make a candidate entry. You can then copy this into the kb/dppkb.yaml, or
you can manually tweak it, or ask claude to tweak it.

The idea is that as the KB is incrementally built up with high quality examples, there will be
less need for manual tweaking, RAG will be good enough.

Also recall we can enhance in future steps

### Adding evidence

`make tmp/with-evidence.yaml`

This with run CurateGPT `citeseek` over all assertions, if there is no `evidence` tag it will
query pubmed for supporting/refuting evidence.

### Periodic Review

It is recommended to periodically inspect the file wearing a lead curator role, and to ask for reviews.

Either global reviews:

`curategpt review --model gpt-4o -p db -c disease "{}"  -t patch --primary-key name > tmp/review.patch.yaml`

Or focused, e.g. if you want `pathophysiology` to be fleshed out:

`curategpt -vv review --model gpt-4o -p db -c disease "{}" -Z pathophysiology -P name -t patch --primary-key name --rule "include as many mechanisms and molecular steps as you can" > tmp/pathophys-review.yaml`

The result is a patch file, This can be manually examined, edited, and applied:

`curategpt apply-patch --patch tmp/patch.yaml --primary-key name kb/dppkb.yaml > tmp/patched.kb.yaml`

Do a diff then move it

### YAML normalization

there are different ways to write YAML. Ensure the kb representation is normalized:

`make normalize`

### Linking to ontology term IDs

Currently we use labels not IDs as these are easier for humans reviewing the YAML, and for LLMs.

Grounding is expected to be trivial and highly reliable, will add a simple mappings to every entry.

### End to end automation

TODO

## Running the app

`make app`

This will create a streamlit app where you can chat with the KB, visualize clusters, etc.

