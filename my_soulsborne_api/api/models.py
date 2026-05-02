from django.db import models

# this is where the surface-level information is held, w/ a url for reference
# one Entity contains these fields (mandatory), and each Entity can be linked to:
    # one or more References (optional)
    # one or more Tags (optional)
    # one or more Interpretations (optional)
class Entities(models.Model):
    url = models.CharField(max_length=100)
    item_icon = models.CharField(max_length=100)
    item_name = models.CharField(max_length=50)
    item_use = models.CharField(max_length=150)
    item_availability = models.CharField(max_length=250)
    item_description = models.TextField()
    category_type = models.CharField(max_length=50)
    
    # def __str__(self):
        # return self.id
    
    
# points (AKA, makes References) to other entities
    # e.g., the Soul of Artorias (entity: id=2) mentions the Abyss (entity: id=10)
    # you can connect these two entities together so as to build a more cohesive narrative
    # by linking one as the source, and the other as the target
class References(models.Model):
    source_id = models.ForeignKey(
        Entities, 
        on_delete=models.CASCADE, 
        related_name="has_source_ref", 
        null=True
        )
    target_id = models.ForeignKey(
        Entities, 
        on_delete=models.CASCADE, 
        related_name="has_target_ref",
        null=True
        )
    note = models.CharField(max_length=100, default="")


# reserved for simpler batches of text, as opposed to the real lore bodies
    # e.g., the Witch of Izalith may get the tag(s): 'First Flame', 'Chaos', 'Lord Souls', etc
# Tags = rows of tags; 
# For more, see => class EntityTags
class Tags(models.Model):
    tag = models.CharField(max_length=50, default="")


# because one row can't necessarily carry more than one tag, that's where EntityTags comes in
# EntityTags = tag_id => Tag && tag_id => Entity
# actually links those tags to their respective Entities
class TagsOfEntities(models.Model):
    # one entity can have many tags
    entity = models.ForeignKey(
        Entities, 
        on_delete=models.CASCADE, 
        related_name="has_eID",
        null=True
        )
    # one tag can belong to many entities
    tag = models.ForeignKey(
        Tags, 
        on_delete=models.CASCADE, 
        related_name="has_tID",
        null=True
        )


# each interpretation gets an id and respective entity id, both held in another table
# the meat n' potatoes, where theories are born and hopes/dreams come to die (thanks, Miyazaki)
# For more, see => InterpretationEntities
class Interpretations(models.Model):
    comments = models.CharField(max_length=300, default="")

# like everything Miyzaki makes, theorycrafting just can't be that simple
# each entity can have one or more interpretations, such as the idea behind Hollowing
    # it can be a metaphor for depression and a physical representation of it affecting the body and soul
    # OR it can be part of the in-universe explanation for why you never die, among other factors
class InterpretationOfEntities(models.Model):
    # one entity can have many interpretations
    entity = models.ForeignKey(
        Entities, 
        on_delete=models.CASCADE, 
        null=False
        )
    # one interpreation can relate to many entites
    interpret = models.ForeignKey(
        Interpretations, 
        on_delete=models.CASCADE, 
        null=False
        )
    