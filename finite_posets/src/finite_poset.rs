use std::collections::{HashMap, HashSet};
use std::hash::{Hash, Hasher};

struct Element {
    label: String,
}

impl PartialEq for Element {
    fn eq(&self, other: &Self) -> bool {
        self.label == other.label
    }
}

impl Hash for Element {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.label.hash(state);
    }
}

struct Poset {
    elements: HashSet<Element>,                         // Set of elements
    porder: HashMap<Element, HashSet<Element>>,      // Hashmap representing the partial order
}

impl Poset {
    fn new() -> Self {
        Poset {
            elements: HashSet::new(),
            porder::HashMap::new(),
        }
    }

    fn add_element(&mut self, element: Element) {
        self.elements.insert(element.clone());
        self.porder.entry(element).or_insert(HashSet::new());
    }


