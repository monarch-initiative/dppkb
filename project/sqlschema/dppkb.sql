-- # Class: "Any" Description: ""
--     * Slot: id Description: 
-- # Class: "Subtype" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: review_notes Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "EvidenceItem" Description: ""
--     * Slot: id Description: 
--     * Slot: reference Description: 
--     * Slot: supports Description: 
--     * Slot: snippet Description: 
--     * Slot: explanation Description: 
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: Prevalence_id Description: Autocreated FK slot
--     * Slot: ProgressionInfo_id Description: Autocreated FK slot
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: Phenotype_name Description: Autocreated FK slot
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: Treatment_name Description: Autocreated FK slot
--     * Slot: InfectiousAgent_name Description: Autocreated FK slot
--     * Slot: Transmission_name Description: Autocreated FK slot
--     * Slot: Diagnosis_name Description: Autocreated FK slot
--     * Slot: Inheritance_name Description: Autocreated FK slot
-- # Class: "Prevalence" Description: ""
--     * Slot: id Description: 
--     * Slot: subtype Description: 
--     * Slot: population Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: percentage_id Description: 
-- # Class: "ProgressionInfo" Description: ""
--     * Slot: id Description: 
--     * Slot: phase Description: 
--     * Slot: subtype Description: 
--     * Slot: age_range Description: 
--     * Slot: incubation_days Description: 
--     * Slot: review_notes Description: 
--     * Slot: incubation_years Description: 
--     * Slot: notes Description: 
--     * Slot: duration_days Description: 
--     * Slot: duration Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Pathophysiology" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: role Description: 
--     * Slot: consequence Description: 
--     * Slot: gene Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Phenotype" Description: ""
--     * Slot: category Description: 
--     * Slot: name Description: 
--     * Slot: diagnostic Description: 
--     * Slot: context Description: 
--     * Slot: review_notes Description: 
--     * Slot: severity Description: 
--     * Slot: notes Description: 
--     * Slot: subtype Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: frequency_id Description: 
-- # Class: "Biochemical" Description: ""
--     * Slot: name Description: 
--     * Slot: presence Description: 
--     * Slot: specificity Description: 
--     * Slot: notes Description: 
--     * Slot: context Description: 
--     * Slot: subtype Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: frequency_id Description: 
-- # Class: "Genetic" Description: ""
--     * Slot: name Description: 
--     * Slot: presence Description: 
--     * Slot: association Description: 
--     * Slot: review_notes Description: 
--     * Slot: subtype Description: 
--     * Slot: features Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: frequency_id Description: 
-- # Class: "Environmental" Description: ""
--     * Slot: name Description: 
--     * Slot: presence Description: 
--     * Slot: notes Description: 
--     * Slot: description Description: 
--     * Slot: effect Description: 
--     * Slot: review_notes Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Disease" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: category Description: 
--     * Slot: notes Description: 
--     * Slot: DiseaseCollection_id Description: Autocreated FK slot
-- # Class: "Treatment" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: context Description: 
--     * Slot: review_notes Description: 
--     * Slot: role Description: 
--     * Slot: notes Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "InfectiousAgent" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Transmission" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: notes Description: 
--     * Slot: effect Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Assay" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
-- # Class: "Diagnosis" Description: ""
--     * Slot: name Description: 
--     * Slot: presence Description: 
--     * Slot: notes Description: 
--     * Slot: results Description: 
--     * Slot: markers Description: 
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Inheritance" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: "Variant" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: Genetic_name Description: Autocreated FK slot
-- # Class: "Mechanism" Description: ""
--     * Slot: name Description: 
--     * Slot: description Description: 
--     * Slot: Treatment_name Description: Autocreated FK slot
-- # Class: "DiseaseCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "Subtype_locations" Description: ""
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: locations Description: 
-- # Class: "Subtype_geography" Description: ""
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: geography Description: 
-- # Class: "Pathophysiology_cell_types" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: cell_types Description: 
-- # Class: "Pathophysiology_biological_processes" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: biological_processes Description: 
-- # Class: "Pathophysiology_locations" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: locations Description: 
-- # Class: "Pathophysiology_examples" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: examples Description: 
-- # Class: "Pathophysiology_pathways" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: pathways Description: 
-- # Class: "Pathophysiology_downstream" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: downstream Description: 
-- # Class: "Pathophysiology_genes" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "Pathophysiology_subtypes" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: subtypes Description: 
-- # Class: "Pathophysiology_cellular_components" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: cellular_components Description: 
-- # Class: "Pathophysiology_chemical_entities" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: chemical_entities Description: 
-- # Class: "Pathophysiology_triggers" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: triggers Description: 
-- # Class: "Pathophysiology_assays" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: assays Description: 
-- # Class: "Pathophysiology_mechanisms" Description: ""
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: mechanisms Description: 
-- # Class: "Phenotype_sequelae" Description: ""
--     * Slot: Phenotype_name Description: Autocreated FK slot
--     * Slot: sequelae Description: 
-- # Class: "Biochemical_cell_types" Description: ""
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: cell_types Description: 
-- # Class: "Biochemical_assays" Description: ""
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: assays Description: 
-- # Class: "Biochemical_synonyms" Description: ""
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: synonyms Description: 
-- # Class: "Environmental_chemicals" Description: ""
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: chemicals Description: 
-- # Class: "Environmental_synonyms" Description: ""
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: synonyms Description: 
-- # Class: "Environmental_examples" Description: ""
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: examples Description: 
-- # Class: "Disease_parents" Description: ""
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: parents Description: 
-- # Class: "Disease_categories" Description: ""
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: categories Description: 
-- # Class: "Disease_synonyms" Description: ""
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: synonyms Description: 

CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Assay" (
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (name)
);
CREATE TABLE "DiseaseCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Disease" (
	name TEXT NOT NULL, 
	description TEXT, 
	category TEXT, 
	notes TEXT, 
	"DiseaseCollection_id" INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("DiseaseCollection_id") REFERENCES "DiseaseCollection" (id)
);
CREATE TABLE "Subtype" (
	name TEXT NOT NULL, 
	description TEXT, 
	review_notes TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Prevalence" (
	id INTEGER NOT NULL, 
	subtype TEXT, 
	population TEXT, 
	"Disease_name" TEXT, 
	percentage_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name), 
	FOREIGN KEY(percentage_id) REFERENCES "Any" (id)
);
CREATE TABLE "ProgressionInfo" (
	id INTEGER NOT NULL, 
	phase VARCHAR, 
	subtype TEXT, 
	age_range TEXT, 
	incubation_days TEXT, 
	review_notes TEXT, 
	incubation_years TEXT, 
	notes TEXT, 
	duration_days TEXT, 
	duration TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Pathophysiology" (
	name TEXT NOT NULL, 
	description TEXT, 
	role TEXT, 
	consequence TEXT, 
	gene VARCHAR, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Phenotype" (
	category TEXT, 
	name TEXT NOT NULL, 
	diagnostic BOOLEAN, 
	context TEXT, 
	review_notes TEXT, 
	severity TEXT, 
	notes TEXT, 
	subtype TEXT, 
	"Disease_name" TEXT, 
	frequency_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name), 
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);
CREATE TABLE "Biochemical" (
	name TEXT NOT NULL, 
	presence TEXT, 
	specificity TEXT, 
	notes TEXT, 
	context TEXT, 
	subtype TEXT, 
	"Disease_name" TEXT, 
	frequency_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name), 
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);
CREATE TABLE "Genetic" (
	name TEXT NOT NULL, 
	presence TEXT, 
	association TEXT, 
	review_notes TEXT, 
	subtype TEXT, 
	features TEXT, 
	"Disease_name" TEXT, 
	frequency_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name), 
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);
CREATE TABLE "Environmental" (
	name TEXT NOT NULL, 
	presence TEXT, 
	notes TEXT, 
	description TEXT, 
	effect TEXT, 
	review_notes TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Treatment" (
	name TEXT NOT NULL, 
	description TEXT, 
	context TEXT, 
	review_notes TEXT, 
	role TEXT, 
	notes TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "InfectiousAgent" (
	name TEXT NOT NULL, 
	description TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Transmission" (
	name TEXT NOT NULL, 
	description TEXT, 
	notes TEXT, 
	effect TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Diagnosis" (
	name TEXT NOT NULL, 
	presence TEXT, 
	notes TEXT, 
	results TEXT, 
	markers TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Disease_parents" (
	"Disease_name" TEXT, 
	parents TEXT, 
	PRIMARY KEY ("Disease_name", parents), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Disease_categories" (
	"Disease_name" TEXT, 
	categories TEXT, 
	PRIMARY KEY ("Disease_name", categories), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Disease_synonyms" (
	"Disease_name" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("Disease_name", synonyms), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Inheritance" (
	name TEXT NOT NULL, 
	description TEXT, 
	"Genetic_name" TEXT, 
	"Disease_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name), 
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);
CREATE TABLE "Variant" (
	name TEXT NOT NULL, 
	description TEXT, 
	"Genetic_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name)
);
CREATE TABLE "Mechanism" (
	name TEXT NOT NULL, 
	description TEXT, 
	"Treatment_name" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name)
);
CREATE TABLE "Subtype_locations" (
	"Subtype_name" TEXT, 
	locations VARCHAR, 
	PRIMARY KEY ("Subtype_name", locations), 
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name)
);
CREATE TABLE "Subtype_geography" (
	"Subtype_name" TEXT, 
	geography VARCHAR, 
	PRIMARY KEY ("Subtype_name", geography), 
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name)
);
CREATE TABLE "Pathophysiology_cell_types" (
	"Pathophysiology_name" TEXT, 
	cell_types VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", cell_types), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_biological_processes" (
	"Pathophysiology_name" TEXT, 
	biological_processes VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", biological_processes), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_locations" (
	"Pathophysiology_name" TEXT, 
	locations VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", locations), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_examples" (
	"Pathophysiology_name" TEXT, 
	examples TEXT, 
	PRIMARY KEY ("Pathophysiology_name", examples), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_pathways" (
	"Pathophysiology_name" TEXT, 
	pathways VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", pathways), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_downstream" (
	"Pathophysiology_name" TEXT, 
	downstream TEXT, 
	PRIMARY KEY ("Pathophysiology_name", downstream), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_genes" (
	"Pathophysiology_name" TEXT, 
	genes VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", genes), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_subtypes" (
	"Pathophysiology_name" TEXT, 
	subtypes TEXT, 
	PRIMARY KEY ("Pathophysiology_name", subtypes), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_cellular_components" (
	"Pathophysiology_name" TEXT, 
	cellular_components VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", cellular_components), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_chemical_entities" (
	"Pathophysiology_name" TEXT, 
	chemical_entities VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", chemical_entities), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_triggers" (
	"Pathophysiology_name" TEXT, 
	triggers VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", triggers), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_assays" (
	"Pathophysiology_name" TEXT, 
	assays VARCHAR, 
	PRIMARY KEY ("Pathophysiology_name", assays), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Pathophysiology_mechanisms" (
	"Pathophysiology_name" TEXT, 
	mechanisms TEXT, 
	PRIMARY KEY ("Pathophysiology_name", mechanisms), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);
CREATE TABLE "Phenotype_sequelae" (
	"Phenotype_name" TEXT, 
	sequelae TEXT, 
	PRIMARY KEY ("Phenotype_name", sequelae), 
	FOREIGN KEY("Phenotype_name") REFERENCES "Phenotype" (name)
);
CREATE TABLE "Biochemical_cell_types" (
	"Biochemical_name" TEXT, 
	cell_types VARCHAR, 
	PRIMARY KEY ("Biochemical_name", cell_types), 
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name)
);
CREATE TABLE "Biochemical_assays" (
	"Biochemical_name" TEXT, 
	assays VARCHAR, 
	PRIMARY KEY ("Biochemical_name", assays), 
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name)
);
CREATE TABLE "Biochemical_synonyms" (
	"Biochemical_name" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("Biochemical_name", synonyms), 
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name)
);
CREATE TABLE "Environmental_chemicals" (
	"Environmental_name" TEXT, 
	chemicals TEXT, 
	PRIMARY KEY ("Environmental_name", chemicals), 
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);
CREATE TABLE "Environmental_synonyms" (
	"Environmental_name" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("Environmental_name", synonyms), 
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);
CREATE TABLE "Environmental_examples" (
	"Environmental_name" TEXT, 
	examples TEXT, 
	PRIMARY KEY ("Environmental_name", examples), 
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);
CREATE TABLE "EvidenceItem" (
	id INTEGER NOT NULL, 
	reference TEXT, 
	supports VARCHAR(15), 
	snippet TEXT, 
	explanation TEXT, 
	"Subtype_name" TEXT, 
	"Prevalence_id" INTEGER, 
	"ProgressionInfo_id" INTEGER, 
	"Pathophysiology_name" TEXT, 
	"Phenotype_name" TEXT, 
	"Biochemical_name" TEXT, 
	"Genetic_name" TEXT, 
	"Environmental_name" TEXT, 
	"Treatment_name" TEXT, 
	"InfectiousAgent_name" TEXT, 
	"Transmission_name" TEXT, 
	"Diagnosis_name" TEXT, 
	"Inheritance_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name), 
	FOREIGN KEY("Prevalence_id") REFERENCES "Prevalence" (id), 
	FOREIGN KEY("ProgressionInfo_id") REFERENCES "ProgressionInfo" (id), 
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name), 
	FOREIGN KEY("Phenotype_name") REFERENCES "Phenotype" (name), 
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name), 
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name), 
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name), 
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name), 
	FOREIGN KEY("InfectiousAgent_name") REFERENCES "InfectiousAgent" (name), 
	FOREIGN KEY("Transmission_name") REFERENCES "Transmission" (name), 
	FOREIGN KEY("Diagnosis_name") REFERENCES "Diagnosis" (name), 
	FOREIGN KEY("Inheritance_name") REFERENCES "Inheritance" (name)
);