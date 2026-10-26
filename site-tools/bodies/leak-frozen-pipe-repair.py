SLUG = 'leak-frozen-pipe-repair'
SERVICE_NAME = 'Leaks & Frozen Pipes'
KEYWORD = 'pipe repair'
SECONDARY_KEYWORDS = ['frozen pipe', 'burst pipe', 'leaking pipe', 'hidden leak']
TITLE = 'Frozen Pipe Repair in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Leak and frozen pipe repair in New Milford, Danbury and nearby CT towns. Fast response, often '
               'without opening walls. Licensed master plumber.')
IMAGE = None

HERO = dict(
    eyebrow='Leaks &amp; frozen pipes · New Milford, CT',
    h1='Leak &amp; frozen pipe repair in New Milford, CT',
    lead=('Pipe frozen, burst or leaking? Shut off your water and call. We find the problem fast, thaw and repair '
          'pipes, often without opening your walls, and help you keep it from happening again.'),
    cta='Get help with a leak',
    panel=dict(title='Leak &amp; freeze problems we fix', items=[
        'Frozen pipes with no water',
        'Burst and split pipes',
        'Leaking pipes and fittings',
        'Hidden leaks causing damage',
        'Pinhole leaks in copper',
        'Outdoor spigots that froze'],
        call_text='Water leaking now? Shut off the main, then call.'),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What leak and frozen pipe repair involves',
         intro=('A frozen or leaking pipe needs fast, careful work. The goal is to stop the water, find exactly where '
                'the problem is and repair it with as little damage to your home as possible.'),
         paras=['Every leak or frozen pipe repair includes:'],
         blocks=[dict(type='checklist', items=[
             'Helping you shut off the water safely',
             'Locating the frozen section or leak',
             'Thawing frozen pipes safely, without open flame',
             'Repairing or replacing damaged pipe and fittings',
             'Working without opening walls whenever possible',
             'Restoring water and checking for other leaks',
             'Finding why it froze or leaked',
             'Recommending fixes to prevent it next time'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Signs of a leaking or frozen pipe',
         intro='Catch these early and you can avoid serious water damage:',
         blocks=[dict(type='cards', cols=3, items=[
             ('No water on a cold morning', 'If one faucet or the whole house has no water during a cold snap, a pipe has likely frozen.'),
             ('Frost or bulging on a pipe', 'Visible frost or a bulge means the pipe is frozen and may already be split.'),
             ('Water stains or soft drywall', 'Stains on ceilings or walls and soft spots usually mean a hidden leak.'),
             ('Running water sounds', 'Hearing water when nothing is on can point to a leak inside a wall or floor.'),
             ('Higher water bills or a busy well pump', 'A pump that runs more than usual or a jump in your bill can mean water is leaking somewhere.'),
             ('Blue-green stains on copper', 'Corrosion on copper pipes, often from acidic well water, can lead to pinhole leaks.')])],
         callout=('<strong>If a pipe bursts:</strong> turn off your main water shut-off right away, turn off power '
                  'to anything electrical near the water if it&rsquo;s safe, and call us. Never thaw a pipe with an '
                  'open flame.')),
    dict(id='options', eyebrow='Repair options', h2='Frozen and leaking pipe repair options',
         intro='The right fix depends on where the problem is and what caused it:',
         blocks=[dict(type='options', items=[
             ('Frozen pipes', 'Safe thawing', 'Frozen sections are thawed with controlled heat and checked for splits before the water is turned back on.', ['No open flames', 'Checks for hidden cracks', 'Water restored safely']),
             ('Most common', 'Leak &amp; section repair', 'The damaged pipe or fitting is cut out and replaced with a durable repair.', ['Targeted repair', 'Minimal disruption', 'Tested under pressure']),
             ('Less damage', 'Repairs without opening walls', 'Whenever we can, we reach and repair pipes through existing access instead of cutting into finished walls.', ['Less drywall damage', 'Faster repair', 'Lower total cost']),
             ('Prevention', 'Freeze protection', 'Insulation, re-routing exposed lines and frost-free outdoor spigots to stop the same pipe from freezing again.', ['Insulated problem spots', 'Frost-free sillcocks', 'Fewer winter emergencies'])])]),
    dict(id='considerations', eyebrow='Prevention', h2='How to prevent frozen and leaking pipes',
         intro='Connecticut winters are hard on plumbing. These steps make a big difference:',
         blocks=[dict(type='consider', items=[
             ('Exposed pipes', 'Pipes in crawl spaces, garages, attics and outside walls freeze first. Insulating them is the simplest protection.'),
             ('Outdoor spigots', 'Disconnect hoses in fall and shut off and drain outdoor spigots, or upgrade to frost-free sillcocks.'),
             ('Cold snaps', 'On the coldest nights, open cabinet doors on outside walls and let a faucet drip to keep water moving.'),
             ('Away from home', 'Keep the heat on when you travel, and know how to shut off your main water valve.'),
             ('Water quality', 'Acidic well water slowly thins copper pipe. Treating it prevents pinhole leaks.'),
             ('Know your shut-off', 'Find and test your main shut-off now, before you need it in an emergency.')])]),
    dict(id='process', eyebrow='How it works', h2='Our pipe repair process',
         intro='Fast response, careful repair and a plan to keep it from happening again.',
         blocks=[dict(type='steps', items=[
             ('Call us', 'Shut off the water if you can, then call. We typically respond within 2&ndash;3 hours.'),
             ('Locate &amp; assess', 'We find the frozen section or leak and check for damage nearby.'),
             ('Clear price', 'You get a clear price for the repair before work starts.'),
             ('Repair &amp; restore', 'We thaw and repair the pipe, restore water and check for other leaks.'),
             ('Prevent', 'We explain what caused it and how to keep it from happening again.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners call us for leaks and frozen pipes',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Pipe repair in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we repair leaking, frozen and burst pipes for homeowners across Western Connecticut, '
             'from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. When a pipe freezes on a '
             'January morning, a local plumber who can get there quickly makes all the difference.')

ESTIMATE = dict(
    heading='Get help with a leak or frozen pipe',
    lead=('Tell us what&rsquo;s happening and where. For active leaks, shut off your water and call us directly for '
          'the fastest response.'),
    options=[('Leak Repair', 'Leaking pipe or fitting'), ('Frozen Pipe', 'Frozen pipe'), ('Burst Pipe', 'Burst pipe'),
             ('Hidden Leak', 'Possible hidden leak'), ('Freeze Prevention', 'Freeze protection'), ('Other', 'Something else')],
    details_label='Tell us what&rsquo;s happening',
    placeholder='e.g. &quot;No water in the kitchen this morning. The pipe runs along an outside wall in the basement.&quot;',
)
REVIEW = dict(quote='He fixed a frozen pipe without opening my walls and gave us a great price. He was efficient and very knowledgeable.',
              name='Erica M.', initials='EM', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Leak &amp; frozen pipe FAQ'
FAQ_HEADING = 'Pipe repair questions, answered.'
FAQS = [
    ('How much does frozen or leaking pipe repair cost?',
     'It depends on where the pipe is, how much is damaged and whether it can be reached without opening walls. '
     'Thawing an exposed pipe costs far less than repairing a burst pipe inside a finished wall. You get a clear price '
     'before the repair starts.'),
    ('What should I do if a pipe bursts?',
     'Turn off the main water shut-off right away, turn off power to anything electrical near the water if it is safe, '
     'move belongings out of the way and call us at <a href="tel:+18602481218">1 (860) 248-1218</a>.'),
    ('Can you fix a frozen pipe without opening the wall?',
     'Often, yes. Many frozen pipes can be thawed and repaired through existing access points. If a pipe has split '
     'inside a wall, a small opening may be needed, and we keep it as small as possible.'),
    ('How do I know if a pipe is frozen?',
     'No water or only a trickle from a faucet during cold weather is the most common sign. You may also see frost on '
     'an exposed pipe. Keep the faucet open and call us. Never use an open flame to thaw a pipe.'),
    ('How quickly can you come out?',
     'We typically respond within 2&ndash;3 hours across New Milford and the surrounding towns. For leaks and frozen '
     'pipes, calling is the fastest way to reach us.'),
]

RELATED_HEADING = 'Other services after a leak or freeze.'
RELATED = [
    ('plumbing-repairs', 'Leaks, valves, fixtures and pressure problems throughout your home, diagnosed and fixed.'),
    ('water-filtration-treatment', 'Treatment for acidic well water that causes pinhole leaks in copper pipes.'),
    ('water-heater-installation', 'Leaking water heaters repaired or replaced, with tank and tankless options.'),
]

CTA = dict(h2='Leaking or frozen pipe?',
           p='Shut off your water and call now. We find the problem fast and give you a clear price for the repair.',
           button='Request help now')
