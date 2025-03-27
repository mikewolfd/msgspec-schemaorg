from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.thing.BioChemEntity import BioChemEntity
    from msgspec_schemaorg.models.thing.Gene import Gene
    from msgspec_schemaorg.models.thing.MedicalCondition import MedicalCondition
    from msgspec_schemaorg.models.thing.Taxon import Taxon


class Protein(Struct, frozen=True):
    """Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type :Protein. A protein can thus be a subclass of another protein, e.g. :Protein as a UniProt record can have multiple isoforms inside it which would also be :Protein. They can be imagined, synthetic, hypothetical or naturally occurring."""
    name: str | None = None
    mainEntityOfPage: str | 'CreativeWork' | None = None
    url: str | None = None
    disambiguatingDescription: str | None = None
    identifier: str | 'PropertyValue' | str | None = None
    description: str | 'TextObject' | None = None
    subjectOf: 'Event' | 'CreativeWork' | None = None
    alternateName: str | None = None
    additionalType: str | str | None = None
    potentialAction: 'Action' | None = None
    sameAs: str | None = None
    image: 'ImageObject' | str | None = None
    bioChemSimilarity: 'BioChemEntity' | None = None
    hasRepresentation: 'PropertyValue' | str | str | None = None
    hasBioChemEntityPart: 'BioChemEntity' | None = None
    taxonomicRange: str | 'DefinedTerm' | str | 'Taxon' | None = None
    funding: 'Grant' | None = None
    isEncodedByBioChemEntity: 'Gene' | None = None
    isInvolvedInBiologicalProcess: 'PropertyValue' | 'DefinedTerm' | str | None = None
    associatedDisease: 'MedicalCondition' | str | 'PropertyValue' | None = None
    bioChemInteraction: 'BioChemEntity' | None = None
    isLocatedInSubcellularLocation: 'PropertyValue' | 'DefinedTerm' | str | None = None
    hasMolecularFunction: 'PropertyValue' | 'DefinedTerm' | str | None = None
    biologicalRole: 'DefinedTerm' | None = None
    isPartOfBioChemEntity: 'BioChemEntity' | None = None
    hasBioPolymerSequence: str | None = None