# dppkb

Disease Pathophysiology Knowledge Base FOR DEMO PURPOSES

This repo contains a mostly automated demo KB of diseases, pathophysiology, treatments,
etiology etc generated using DRAGON-AI/CurateGPT.

The KB is created via a cycle:

1. Human expert creates one or two seed entries
2. New entries are created from latent knowledgebase of LLM
3. Pubmed is searched for support/refute evidence on a per-assertion basis
4. LLM acts as critic guided by human to constantly refine

## Website

[https://monarch-initiative.github.io/dppkb](https://monarch-initiative.github.io/dppkb)

Click on "Diseases" to browse the "Knowledge Base". You will see a highly generic
rendering of auto-generated disease entries.

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

Note: this loads a pre-processed version that has the evidence removed; we want to
hide this when doing RAG as we want to avoid publication hallucination.

### Generate a new entity

Run this:

`make tmp/complete-Tuberculosis.yaml`

This uses RAG/DRAGON-AI to make a candidate entry. You can then copy this into the kb/dppkb.yaml, or
you can manually tweak it, or ask claude to tweak it.

The idea is that as the KB is incrementally built up with high quality examples, there will be
less need for manual tweaking, RAG will be good enough.

Also recall we can enhance in future steps

NOTE: This step does not use the pubmed directly. We are relying on the fact that the LLM has already ingested
and compressed all the literature and can do a pretty good first-pass job at re-exporting that in any
format we like. It doesn't have to be perfect though, subsequent steps are designed to refine this.

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

### Clustering

Ask a question:

<img width="785" alt="image" src="https://github.com/monarch-initiative/dppkb/assets/50745/40fef947-3bd9-4c28-9a3f-3345c41026c2">

See results clustered:

<img width="770" alt="image" src="https://github.com/monarch-initiative/dppkb/assets/50745/10eb74f0-9861-459a-9188-2494b5b250b3">

### Chat

<img width="696" alt="image" src="https://github.com/monarch-initiative/dppkb/assets/50745/fca67f84-31b9-44ed-b157-4644d6a15297">

results:

<img width="767" alt="image" src="https://github.com/monarch-initiative/dppkb/assets/50745/c09926a6-6d58-42fa-a841-d5c0a77158e6">

<img width="705" alt="image" src="https://github.com/monarch-initiative/dppkb/assets/50745/17b495ad-3dd9-4bf1-82b4-278c6e7f2e0e">



