ignore = data.get("domains_to_ignore","zone,group,automation,script,zwave")
domains_to_ignore=ignore.split(",")
target_group=data.get("target_group","group.catchall")

logger.info("ignoring {} domain(s)".format(len(domains_to_ignore)))
logger.info("Targetting group {}".format(target_group))

def scan_for_new_entities(hass, logger, domains_to_ignore, target_group):
  entity_ids=[]
  groups=[]
  catchall=hass.states.get(target_group)

  if (catchall is None):
    logger.error("Target group {} doesn't exist".format(target_group))
    return
  
  for state in hass.states.all():
    domain = state.entity_id.split(".")[0]
    if (domain not in domains_to_ignore):
      entity_ids.append(state.entity_id)
    if (domain == "group") and (state.entity_id != target_group):
      groups.append(state.entity_id)
    

  logger.info("==== Entity count ====")
  logger.info("{0} entities".format(len(entity_ids)))
  logger.info("{0} groups".format(len(groups)))

  for groupname in groups:
    group = hass.states.get(groupname)
    for a in group.attributes["entity_id"]:
      if a in entity_ids:
        entity_ids.remove(a)

  attrs={}
  for a in catchall.attributes:
    if a != "entity_id":
      attrs[a] = catchall.attributes[a]

  entity_ids.insert(0,"script.scan_for_new_devices")
  attrs["entity_id"]=entity_ids
  hass.states.set("group.catchall", catchall.state, attrs)

scan_for_new_entities(hass, logger, domains_to_ignore, target_group)